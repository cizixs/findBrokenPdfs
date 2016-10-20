# coding: utf-8

import logging
import os
import sys

import pdfrw
from tqdm import tqdm


# disable third-party library logging output
logging.disable(logging.CRITICAL)


def find_all_pdfs(path):
    """Use os.walk to traverse all pdf files"""
    pdfs = []
    for root, dirs, files in os.walk(path):
        found = [os.path.join(root, f) for f in files if f.endswith("pdf")]
        pdfs.extend(found)
    return pdfs


def is_valid_pdf(fname):
    """Check the pdf file is valid.

    A pdf file is only valid if it can be open with pdfrw with on error
    """
    try:
        pdfrw.PdfReader(fname)
    except pdfrw.PdfParseError:
        return False
    except Exception:
        return True
    return True


def delete_files(files):
    for fname in files:
        os.remove(fname)


def main(path):
    # TODO(cizixs): path parse, ".", "~" expand, validation
    broken_pdfs = []
    pdfs = find_all_pdfs(path)
    print("{} pdfs found.".format(len(pdfs)))

    pbar = tqdm(pdfs)
    for pdf in pbar:
        # pbar.set_description("Process %s" % pdf)
        if not is_valid_pdf(pdf):
            pbar.write("Broken: %s" % pdf)
            broken_pdfs.append(pdf)

    if len(broken_pdfs) > 0:
        n = len(broken_pdfs)
        # print("%d broken pdfs found." % n)
        answer = raw_input("%d broken pdfs found. Delete them?(yes or no)" % n)
        if answer.lower() in ["y", "yes", "ok"]:
            delete_files(broken_pdfs)
            print("%d files delted." % len(broken_pdfs))


def usage():
    print("Usage: %s path\n" % sys.argv[0])
    print("Scan broken pdf files.\n")
    print("positional arguments:")
    print("  path         directory to scan")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    main(sys.argv[1])

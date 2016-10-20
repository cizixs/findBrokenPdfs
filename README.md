# findBrokenPdfs

This is a command line tool to find broken(unable to open) pdf documents, 
and delete them if you wish.


    ➜  findBrokenPdfs python main.py /Users/cizixs/Documents
    255 pdfs found.
    Broken: /Users/cizixs/Documents/Books/Learning UML 2.0.pdf
    Broken: /Users/cizixs/Documents/Books/Node.js in Action.pdf
    Broken: /Users/cizixs/Documents/Books/PowerShell and WMI.pdf
    Broken: /Users/cizixs/Documents/Books/PowerShell in Depth, 2nd Edition.pdf
    Broken: /Users/cizixs/Documents/Books/Pro DNS and BIND 10.pdf
    Broken: /Users/cizixs/Documents/Books/Python for Data Analysis.pdf
    Broken: /Users/cizixs/Documents/Books/Python Machine Learning.pdf
    Broken: /Users/cizixs/Documents/Books/The Browser Hacker's Handbook.pdf
    Broken: /Users/cizixs/Documents/Books/Windows PowerShell in Action, 2nd Edition.pdf
    Broken: /Users/cizixs/Documents/技术/TransofLPTG.pdf
    100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 255/255 [00:51<00:00,  4.94it/s]
    10 broken pdfs found. Delete them?(yes or no)yes
    10 files delted.


# Usage
Run the script and pass the directory you want to scan.

    Usage: main.py path
    
    Scan broken pdf files.
    
    positional arguments:
      path         directory to scan


# Todos

- [ ] delete broken pdfs by default without asking
- [ ] support multi directories scan
- [ ] speed up the whole process with concurrency programming
- [ ] non-recursive scanning(only scan the directory, not its inner directories)
- [ ] write setup.py and upload to pypi

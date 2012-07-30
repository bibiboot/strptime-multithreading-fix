strptime-multithreading-fix
===========================

Strptime multi threading issue replication and its solution.

Issue
===========================

Python's strptime when access by more then one threads simultaneously, it only allows the execution of one thread and throws exception at rest of the other threads.

Reason
===========================

Python's strptime is not threadsafe therefore to implement multi threading strptime uses `ImportModuleNoBlock` to drop another thread if its executing a thread.

Fix
===========================

A hack which works is by calling the strptime well before the creation of the threads.
In a web application, the strptime dummy call can be added in the wsgi file.

Run
===========================

    # To replicate the issue
    python strptime_issue.py Replicate

    # To fix the issue
    python strptime_issue.py Fix

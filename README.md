1) Generate a small file:
```bash
head -c 1K </dev/urandom >smalldata
```

2) Generate a big file:
```bash
head -c 1G </dev/urandom >bigdata
```

3) Run the script against the small data
```bash
python writer.py smalldata
```

4) Run the script against the big file
```bash
python writer.py bigdata
```

Note 1: With Python 2.7, step 3 will often block forever but sometimes will finish and step 4 will always block forever.
Note 2: WIth Python 2.7 and subprocess32 installed, both step 3 and 4 finish without blocking.
Note 3: Using Python 3.6, both step 3 and 4 finish without blocking.


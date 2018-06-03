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

Notes: Step 3 will often block but sometimes will finish. Step 4 always blocks.


# Building Concept Graph

### Dataset
Put all your input text files in **input** directory

### To run

```bash
python main.py
```

### Output
It will create following directory structure:
```bash
--- processed
--- dict_and_encoded_texts
--- edges
--- graph
```

### Paramters
You can change below parameteres in main.py
```python
# maximum allowed window size for edge formattion
max_window_size = 5

# number of processes running in parallel
process_num = 5

# minimum threshold frequency of occurrence of a word to be a node
min_count = 1

# maximum number of allowed nodes
max_vocab_size = 100000

safe_files_number_per_processor = 200
```

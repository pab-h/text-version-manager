
# text-version-manager

## The Purpose
This algorithm aims to version a single .txt file using the abstract stack data structure 

## How does it work?
There is a stack that stores the name of a version file of the source file. To create a new version is to push a version object onto a version stack. Restoring a version is to pop the version on the stack and replace the source file.

## CLI

### Require
The fist argument is alwas the path to file.txt
```bash
python path/to/text-version-manager/main.py "path/to/file.txt"
```

### Save a version
```bash
python path/to/text-version-manager/main.py "path/to/file.txt" --save
```

### Restore a version
```bash
python path/to/text-version-manager/main.py "path/to/file.txt" --restore
```
If there is no version to restore. Error.

## TextVersionManager 

### construct
```python
txtVM = TextVersionManager(file = "path/to/file.txt")
```

### save()
This method create a new version of file.txt
```python
txtVM.save() 
```

### restore()
This method restores a version of file.txt
```python
txtVM.restore() 
```

## Future
- [ ] Multiple file versions
- [ ] Multiple text extensions support
- [ ] Error Handling
# ftlookup
Simple wrapper around Facebook fastText

## Requirements

This project needs *Cython* and *numpy*.

## Usage

  import ftlookup

  model = ftlookup.FastTextWrapper() 
  model.loadModel('data/alice.bin')
  print(model.vector_size)
  print(model.getVector('Alice'))

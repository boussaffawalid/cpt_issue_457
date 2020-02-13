# cpt_issue_457

$ export CONAN_OPTIONS="Foobar:with_bar=True,Foobar:with_bar=False"
# python3 build.py


## Actual Output
+-----+-------------+--------+--------------+--------------------+-----------------+-------------------+
|   # | compiler    | arch   | build_type   |   compiler.version | Foobar:shared   | Foobar:with_bar   |
|-----+-------------+--------+--------------+--------------------+-----------------+-------------------|
|   1 | apple-clang | x86_64 | Release      |                 10 | True            | False             |
|   2 | apple-clang | x86_64 | Debug        |                 10 | True            | False             |
|   3 | apple-clang | x86_64 | Release      |                 10 | False           | False             |
|   4 | apple-clang | x86_64 | Debug        |                 10 | False           | False             |
+-----+-------------+--------+--------------+--------------------+-----------------+-------------------+



## Expected Output
+-----+-------------+--------+--------------+--------------------+-----------------+-------------------+
|   # | compiler    | arch   | build_type   |   compiler.version | Foobar:shared   | Foobar:with_bar   |
|-----+-------------+--------+--------------+--------------------+-----------------+-------------------|
|   1 | apple-clang | x86_64 | Release      |                 10 | True            | False             |
|   2 | apple-clang | x86_64 | Debug        |                 10 | True            | False             |
|   3 | apple-clang | x86_64 | Release      |                 10 | False           | False             |
|   4 | apple-clang | x86_64 | Debug        |                 10 | False           | False             |
|   1 | apple-clang | x86_64 | Release      |                 10 | True            | True              |
|   2 | apple-clang | x86_64 | Debug        |                 10 | True            | True              |
|   3 | apple-clang | x86_64 | Release      |                 10 | False           | True              |
|   4 | apple-clang | x86_64 | Debug        |                 10 | False           | True              |
+-----+-------------+--------+--------------+--------------------+-----------------+-------------------+
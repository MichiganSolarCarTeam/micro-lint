# microLint [![PyPI version](https://img.shields.io/pypi/v/microLint.svg)](https://pypi.python.org/pypi/microLint) [![Badges](https://badginator.herokuapp.com/arxanas/microLint.svg)](https://github.com/defunctzombie/badginator)

`microLint` checks your changes for coding style errors.

See https://suckless.org/coding_style/ for some of the rules streamlined. The coding standards
can be found in the Manifesto as well!

Here's `microLint` in action:

![Example microLint usage](media/example.png)

# Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for information on how to contribute to
the project. Patches welcome!

# Usage

`microLint` requires Python 3, so you may want to install it inside a `virtualenv`
or use `pip3` instead of `pip`.

Install it:

    $ pip install microLint

Pass source files to `microLint` to have it check them. Typically you'll just use
a pattern like `*.cpp *.h` to match all source files in the current directory.

    $ microLint *.cpp *.h

If `microLint` detected any errors, it will exit with a non-zero status and print
the errors. Otherwise it will exit with zero and produce no output.

By default, `microLint` assumes your source files are in C++. You can explicitly
set the language with `--lang=c` or `--lang=cpp`:

    $ microLint --lang=c *.c *.h

# Features

## C checks

The C linter flags the following:

  * Use of prohibited types (such as `unsigned` and `float`).
  * Macros that start with an underscore, as they are reserved by the
	implementation.
  * Non-uppercase `#defines` (`#define foo` is wrong, `#define FOO` is right).
  * `struct`s and `enum`s that aren't capitalized.
  * `enum`s that don't end with `_e`.
  * `typedef`s that don't end with `_t`.
  * Non-idiomatic comparison to `NULL` (such as `if (foo == NULL)`).
  * Enum members that aren't all-caps.
  * Casting the result of `malloc` (such as `foo = (char*) malloc(...)`).
  * Defining string constants as an array instead of a pointer.
  * Use of `sizeof(char)`.
  * Putting user includes after system includes.
  * Not including the module header as the first include in the file.

## C++ checks

The C++ linter flags the following:

  * All C checks above, except those that are obviated (e.g. we now use
	`nullptr` instead of `NULL`, and don't use `malloc`).
  * Comments with three asterisks (`***`) as those are provided by Kieras and
	should be removed.
  * Use of `NULL` instead of `nullptr`.
  * Use of `malloc`/`free` instead of `new`/`delete`.
  * Use of `typedef` instead of `using`.
  * Use of prohibited functions such as `memmove` or `exit`.
  * Creating a type alias for an iterator instead of its container (i.e. `using
	Foo_t = std::vector<int>::iterator` instead of `using Foo_t =
std::vector<int>; /* ... */ Foo_t::iterator`).
  * Use of `#define` to create constants.
  * Use of `class` instead of `typename` in template parameters.
  * Use of `0` or `1` in loop conditions instead of `true` or `false`.
  * Use of `string::compare`.
  * Comparing `size()` to `0` instead of using `empty`.
  * Use of post-increment instead of pre-increment for iterators.
  * Catching exceptions by value instead of by reference.
  * Unused `using`-statements, such as `using std::cout;`.
  * Using `enum`s instead of `enum class`es.
  * Naming `enum class`es with a trailing `_e`, which is the convention for C but not C++.
  * Uppercase `enum class` members, which is unnecessary because they are scoped.

# License

`microLint` is licensed under GPLv3.
# Python katas vol.2
My solutions of katas available on codewars.com gathered in one place - Python Edition.
[![CodeWars](https://www.codewars.com/users/Wojcirej/badges/large)](https://www.codewars.com/users/Wojcirej/badges/large "My Honor Badge")

See previous "edition" [here](https://github.com/Wojcirej/python-katas). It will contain some kata solutions, which are present in this repository as well. But in this repo I will use different unit tests framework.

# Set up (virtual) environment
1. Install `virtualenv`:
```bash
sudo pip3 install virtualenv
```
2. Create directory for you local, virtual python environments:
```bash
mkdir ~/.python-virtual-environments
```
3. Create new python virtual environment named `python-katas` with packages currently available in the system:
```bash
virtualenv --system-site-packages ~/.python-virtual-environments/python-katas
```
4. Activate your virtual environment
```bash
. ~/.python-virtual-environments/python-katas/bin/activate
```

# Launch tests
`pytest`
# Solution generator
`python3 generator.py <kata_name> [argument names]`
### Example of solution generator usage
`python3 generator.py test_kata arg1 arg2`
will generate template for kata with `test_kata` name in `/katas/` directory.

In this case, file within `katas/test_kata/` directory named `test_kata.py` will contain template for function named `test_kata` taking two arguments: `arg1` and `arg2`.

There will be also file template for tests in `/tests/` directory, named `test_<kata_name>.py`, where unit tests should be placed.
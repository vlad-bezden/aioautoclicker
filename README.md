# Auto mouse clicker (autoclicker)

## By default it clicks every 60 seconds

### Usage
* python autoclicker.py

  By default it clicks every 60 seconds and size of the progress bar is 60 chars
* python autoclicker.py -i 10
* autoclicker -i 10 -s 120

  This example will click every 10 seconds

Press 'Enter' key to 'Pause' and 'Resume' autoclicker
To stop running press 'Ctrl'+'C' keys

## Requirements
* Python 3.7 and up

  `pip install -r requirements\prod.txt`

## Developers
  `pip install -r requirements\dev.txt`

* to build a wheel

  `python setup.py bdist_wheel`
* install wheel
  `pip install <wheel>`

## Deployment
1. Create wheel by
`python setup.py bdist_wheel`
2. Copy created wheel from `dist` directory to directory where you going to deploy it
3. Install wheel
`pip install <wheel>`
4. Run it
`autoclicker -i 10`


### Build tips
There are two ways to build weels:
1. using `setuptools.find_packages`
2. explicitly specify packages for distribution

#### Using setuptools.find_package
This option requires `__init__.py` file in a package that has to be distributed. Without this file find_package method will not consider directory as a package

`config.cfg` file configuration:

```
# config.cfg

[options]
packages = find:
```

#### Explicitly specify package
This option is suitable for a small projects. Because packages entered manually, no `__init__.py` file is required in directories that has to be distributed instead in `setup.cfg` file specify directories that has has to be distributed as part of package

```
# config.cfg

[options]
packages = autoclicker
```

# Auto mouse clicker (autoclicker)

## By default it clicks every 60 seconds

### Usage
* python autoclicker.py

  By default it clicks every 60 seconds
* python autoclicker.py -i 10

  This example will click every 10 seconds

Press 'Enter' key to 'Pause' and 'Resume' autoclicker
To stop running press 'Ctrl'+'C' keys

## Requirements
* Python 3.7 and up

  `pip install -r requirements.txt`

## Developers
  `pip install -r requirements_dev.txt`

* to build a wheel

  `python setup.py bdist_wheel`

## Deployment
1. Create wheel by
`python setup.py bdist_wheel`
2. Copy created wheel from `dist` directory to directory where you going to deploy it
3. Install wheel
`pip install autoclicker-2.0.0-py3-none-any.whl`
4. Run it
`autoclicker -i 10`

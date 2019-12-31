# CHRSMA - Backend 
### Chrsma REST api built with python and Flask for CHRSMA Android App

Created by [@dvlp.er](https://www.instagram.com/dvlp.er/) and [@insane.dvlper](https://www.instagram.com/insane.dvlpr/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of contents:
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Development](#development)
4. [Documentation](#documentation)
5. [Contributing](#contributing)
6. [License](#license)


## Requirements:
- python
- Terminal
- Flask
- Some Code editor
- Brain

## Installation:
open terminal and type this command:
```
$ pip install requirements.txt
```
once all the required dependcies are installed, open `app.py` in any code editor
change this line 
```
app.run()
```
to 
```
app.run(debug=True)
```
This will enable you the flask development mode.

## Development
To run the app, type this command in Terminal:
```
$ python app.py
```
Now open the browser and enter `http://127.0.0.1:5000/api/getchrsma?name=waseem&gender=male&age=20`

## Documentation:
**route**: 
`/api/getchrsma`

**query**:
- name [ your name ]
- gender [ male | female ]
- age [5 > age < 100 ]

**return**: 
type: JSON
```
{
  success:...,{}
  data:...
  message:...,
}
```
- Success [True | False]
- data [The response]
- message [if any error occured, message will contain description of the error]

## Contributing
We are happy if you add something useful in this project. so feel free add your ideas and make sure you document it.

## License
Licensed under the MIT (see [LICENSE](https://github.com/devwaseem/chrsma-backend/blob/master/LICENSE))

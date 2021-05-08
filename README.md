# PubNub Example

## Prerequisite

* CentOS7+
* Python3.8+

## Preparation

* Install pyenv and Python 3.8.10
* Create venv environment
* Install requirements

### pyenv

Please refer https://github.com/pyenv/pyenv

```shell
$ pyenv install 3.8.10
```

### venv

Please refer https://docs.python.org/3/library/venv.html

```shell
$ python -m venv venv
$ . ./venv/bin/activate
```

### install requirements

```shell
(venv)$ pip install -r requirements.txt
```

## File Transfer Example

This example sends a JPEG image file to PubNub service,
and receive the data from the service and open it as a image.

I used PIL to process images.

### Sample codes

* file_pub.py
  * This sends a file
* file_sub.py
  * This receives a file
* file_list.py
  * This lists files stored in the PubNub service

### Create `param.sh`

Create the param.sh to register environmental variables for PubNub keys.
`param.sh` is listed in `.gitignore` file to prevent accidents.

```shell
export PUBNUB_PUBKEY=pub-xxxxxx
export PUBNUB_SUBKEY=sub-xxxxxx
```

Execute `param.sh`

```shell
(venv)$ . param.sh
```

### Send file

```shell
(venv)$ python file_pub.py
```
### List file

```shell
(venv)$ python file_list.py
```

### Receive and open file

```shell
(venv)$ python file_sub.py
```

This sample code uses PIL to open JPG data.

## Messaging

This project includes sample codes: pub.py and sub.py

This are based on the official document's sample codes.
Please refer the documents for use.



<!-- vim: set tw=0 et sts=2 sw=2 ts=2: -->

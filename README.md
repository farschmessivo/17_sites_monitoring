# Sites Monitoring Utility

The script monitors the sites for response the status code and an expiration date.
It checks whether site is expiring in month, and whether http response status is 200.

To run the script python3.5 is required.
Side packages are listed in requirements.txt. To install packages run the following command in shell:
```bash
$ pip install -r requirements.txt
```

The script takes one positional argument:
* path - the path to file, containing urls of sites for monitoring

## Example of file content

```
http://github.com
https://theframeworks.com
https://google.com
```

# How to run the script

```
$ python3 check_sites_health.py <txt_with_utls> 

Checking http://github.com
	Server respond with 200: True
	Expiring in month: False

Checking http://romangagarin.com
	Server respond with 200: True
	Expiring in month: True

Checking http://theframeworks.com
	Server respond with 200: True
	Expiring in month: False


```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

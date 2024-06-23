# Mosquitto mqtt actor

## Config
Using template files provided and changing data to corresponding data you can use repository.

`main.py` takes one argument of name config which is yaml file which template is placed in templates directory.

## Using config file
Copy config file to main directory:
```bash
cp templates/config.yaml.template config.yaml
```

Then insert your required credentials

## Pylint
For linux bash pylint is supported via command:
```bash
bash pylint.sh
```

Either way add pylint to IDE or editor to work with project without failing on push.

## Test received frames

To test received frames use command from mosquitto clients library (example, adjust to configuration):
```bash
 mosquitto_pub -t "human-detected" -h "localhost" -m "True"
```

## GPIO Zero
To install library on raspberry pi use:
```bash
sudo apt install python3-gpiozero
```
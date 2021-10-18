# balena BLINKT(!)

![balena BLINKT!](logo.png)

RESTful API for controlling a Raspberry Pi with a BLINKT(!) board attached over balena cloud.

## Hardware required

* Raspberry Pi 3 or 4
* Pimoroni ![BLINKT(!) board](https://shop.pimoroni.com/products/blinkt)
* A 4GB or greater micro SD card (We always recommend SanDisk Extreme Pro SD cards)
* Power supply

## Software required

* A download of this project
* Software to flash an SD card (![balenaEtcher](https://balena.io/etcher))
* A free ![balenaCloud](https://balena.io/cloud) account
* The ![balena CLI tools](https://github.com/balena-io/balena-cli/blob/master/INSTALL.md)

## Setup and use

To run this project is as simple as deploying it to a balenaCloud application, no additional configuration is required.

### Setup the device

* Sign up for or login to the ![balenaCloud dashboard](https://dashboard.balena-cloud.com)
* Create an application, selecting the correct device type for your Raspberry Pi
* Add a device to the application, enabling you to download the OS
* Flash the downloaded OS to your SD card with ![balenaEtcher](https://balena.io/etcher)
* Power up the board and check it's online in the dashboard

### One Click Deployment

You can deploy this server with one click with the button below. Or, you can follow the manual deployment instructions in the next section.

[![Deploy with balena](https://balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/cniweb/balena-python-blinkt.git)

### Manually Deploy this application

* Install the ![balena CLI tools](https://github.com/balena-io/balena-cli/blob/master/INSTALL.md)
* Login with `balena login`
* Download this project and from the project directory run `balena push <appName>` where `<appName>` is the name you gave your balenaCloud application in the first step.

## Usage instructions

You can use the public device URL from your device for controlling the BLINKT(!) board.

### Examples

Turn all light on:

```javascript
https://***.balena-devices.com/on
```

Turn all light off:

```javascript
https://***.balena-devices.com/off
```

Turn all light red:

```javascript
https://***.balena-devices.com/red
```

Turn all light green:

```javascript
https://***.balena-devices.com/green
```

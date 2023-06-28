# Running Shiny for Python apps in ShinyProxy

This repository describes how to add a Shiny for Python app inside ShinyProxy.

# Build the Docker image

To pull the image made in this repository from Docker Hub, use

```bash
sudo docker pull openanalytics/shinyproxy-shiny-for-python-demo
```

the relevant Docker Hub repository can be found at https://hub.docker.com/r/openanalytics/shinyproxy-shiny-for-python-demo

To build the image from the Dockerfile, clone this repository, then navigate to its root directory and run

```bash
sudo docker build -t openanalytics/shinyproxy-shiny-for-python-demo .
```

# ShinyProxy Configuration

To add the Shiny For Python application to ShinyProxy add the following lines to its configuration file (see [application.yml](./application.yml) for a complete file):
```
specs:
  - id: shiny-for-python-demo
    display-name: Shiny For Python Demo Application
    container-image: openanalytics/shinyproxy-shiny-for-python-demo
    port: 8080
```

# References
* https://shiny.posit.co/py/docs/overview.html
* https://matplotlib.org/3.5.3/gallery/userdemo/colormap_interactive_adjustment.html


**(c) Copyright Open Analytics NV, 2023.**

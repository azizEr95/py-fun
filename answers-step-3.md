# Step 3: Questions for the Dev-Container

1. **Where are programs installed in general? Where has make been installed in the container?**
    - On Linux, programs are installed in `/usr/bin` (system packages), `/usr/local/bin` (manual installs) or `/bin`. They are found through `$PATH`.
    - In the container, `make` was installed at `/usr/bin/make` (checked with `which make`).

1. **Containers are meant to be removed and rebuilt frequently. What does this mean for the missing make command?**
    - Anything installed by hand (`apt-get install make`) is lost when the container is rebuilt.
    - It has to be installed again every time, unless it is part of the image.

1. **How can a software package permanently be added to a Docker container?**
    - Add the installation to the `Dockerfile` (e.g. `RUN apt-get update && apt-get install -y make`) and rebuild the image.

1. **What is the purpose of the Dockerfile in .devcontainer?**
    - It is the build recipe for the container image: base system, installed tools, environment and settings.
    - It makes sure every developer gets the same environment.

1. **Briefly describe the effects of FROM, ENV, WORKDIR and RUN.**
    - `FROM`: sets the base image the new image builds on (e.g. a Debian/Python image). `ENV`: sets environment variables in the container.
    - `WORKDIR`: sets the working directory for the following commands and the container. `RUN`: runs a command while the image is built (e.g. installing packages).

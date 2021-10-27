# AppModeInit

This app is a bare bones example of how to launch a server using [Deephaven's application mode](https://deephaven.io/core/docs/how-to-guides/app-mode/).

## How it works

### Components

* `Dockerfile` - The Dockerfile for the application. This extends the default Deephaven image to add the app mode directory.
* `app.d` - The app mode directory. Deephaven expects this to contain at least one `*.app` file.
* `app.d/app.app` - The app mode config file. This defines what type of script to run on launch.
* `app.d/init.py` - The Python script to run on launch.
* `docker-compose.yml` - The docker-compose file for the application. This is mostly the same as the [Deephaven docker-compose file](https://raw.githubusercontent.com/deephaven/deephaven-core/main/containers/python-examples/docker-compose.yml), but with modifications to run app mode, specifically the `-Ddeephaven.application.dir=/app.d` flag being set on the `grpc-api`.
* `start.sh` - A helper script to launch the application.

### High level overview

This app launches a Deephaven server and initializes it with a table containing 5 numbers.

## Dependencies

* The [Deephaven-core dependencies](https://github.com/deephaven/deephaven-core#required-dependencies) are required for this project.

## Launch

Simply run the following to launch the app:

```
sh start.sh
```

Go to [http://localhost:10000/ide](http://localhost:10000/ide) to view the table in the top right **Panels** tab!

# AppModeInit

This app is a bare bones example of how to launch a server using [Deephaven's application mode](https://deephaven.io/core/docs/how-to-guides/app-mode/).

## How it works

### Components

* `data/app.d` - The app mode directory. Deephaven expects this to contain at least one `*.app` file.
* `data/app.d/app.app` - The app mode config file. This defines what type of script to run on launch.
* `data/app.d/init.py` - The Python script to run on launch.
* `docker-compose.yml` - The docker-compose file for the application. This is mostly the same as the [Deephaven docker-compose file](https://raw.githubusercontent.com/deephaven/deephaven-core/main/containers/python-examples/docker-compose.yml), but with modifications to run app mode, specifically the `-Ddeephaven.application.dir=/data/app.d` flag being set on the `server` image.

### High level overview

This app launches a Deephaven server and initializes it with a table containing 5 numbers.

## Dependencies

* The [Deephaven-core dependencies](https://github.com/deephaven/deephaven-core#required-dependencies) are required for this project.

## Launch

Simply run the following to launch the app:

```
docker-compose up
```

Go to [http://localhost:10000/ide](http://localhost:10000/ide) to view the table in the top right **Panels** tab!

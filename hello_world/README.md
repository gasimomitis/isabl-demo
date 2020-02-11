# Configure

To run the app, add to the `$PYTHONPATH` the directory where the `hello_world` module is:

```bash
export PYTHONPATH=`pwd`
```

Then change the client settings:

```bash
export ISABL_CLIENT_ID=4
```

Check the app is avaliable to run:

```bash
isabl apps-grch37 --help
```

# Usage

Run with Isabl

```bash
isabl apps-grch37 \
    hello-world-1.0.0 \
    -fi <filter-for-targets> \
    [--commit]
```

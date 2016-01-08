# MICA within docker

Leverages [mica](https://github.com/boegel/MICA) (and 
[pin](https://software.intel.com/en-us/articles/pintool)) to profile a 
process within a docker container.

To profile:

```bash
./profile \
  -r \
  -i <image>
  -f <docker-run-flags>
  -p <pre-command>
  -c <command>
  -n <name>
```

Arguments:

  * `r` whether to recompile MICA. When passed, `gcc, g++, make` 
    should be available inside the container.
  * `i` image name.
  * `f` flags to be passed to `docker run`.
  * `p` any commands that are executed prior to the one given in `-c`, 
    which are _not_ profiled.
  * `c` command to execute and profile.
  * `n` name to associate to the output


For example, to profile `ls`:

```bash
./profile -i debian:jessie \
          -f "--rm --net=host" \
          -p "cd /var" \
          -c ls \
          -n ls
```

If the `output.csv` file exists, `profile` won't rewrite it; it will 
append rows to it instead.

## Requirements

  * Same requirements as pin/mica: Linux 2.6/3.x, `gcc` 3.4+, 
    single-threaded x86_64 applications.
  * [`jq`](https://stedolan.github.io/jq/) 1.5+
  * Only tested on debian/ubuntu-based docker images.

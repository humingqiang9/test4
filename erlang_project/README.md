# Erlang gen_server Example

This is a simple example of an Erlang gen_server implementation that manages a counter state.

## Files

- `simple_counter.erl` - The main gen_server module
- `test_counter.escript` - A test script to demonstrate usage
- `Makefile` - For easy compilation and cleanup

## Compilation

You can compile the module in two ways:

1. Using erlc directly:
   ```
   erlc simple_counter.erl
   ```

2. Using the Makefile:
   ```
   make
   ```

## Usage

After compilation, you can run the test script:

```
./test_counter.escript
```

Or start an Erlang shell and interact with the gen_server manually:

```
erl
1> simple_counter:start_link().
{ok,<0.85.0>}
2> simple_counter:get_count().
0
3> simple_counter:increment().
ok
4> simple_counter:get_count().
1
```

## Cleanup

To remove compiled beam files:

```
make clean
```
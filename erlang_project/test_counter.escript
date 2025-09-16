#!/usr/bin/env escript

%% Test script for simple_counter gen_server

main(_) ->
    % Start the Erlang distribution
    {ok, _} = application:ensure_all_started(sasl),
    
    % Start the simple_counter gen_server
    {ok, Pid} = simple_counter:start_link(),
    io:format("Started simple_counter gen_server with PID: ~p~n", [Pid]),
    
    % Test the API
    io:format("Initial count: ~p~n", [simple_counter:get_count()]),
    
    simple_counter:increment(),
    simple_counter:increment(),
    io:format("Count after 2 increments: ~p~n", [simple_counter:get_count()]),
    
    simple_counter:decrement(),
    io:format("Count after 1 decrement: ~p~n", [simple_counter:get_count()]),
    
    % Stop the gen_server
    exit(Pid, normal),
    io:format("Stopped simple_counter gen_server~n").
-module(HipyHXwvSP).
-behaviour(gen_server).

%% API
-export([start_link/0, get_count/0, increment/0, decrement/0, set_count/1]).

%% gen_server callbacks
-export([init/1, handle_call/3, handle_cast/2, handle_info/2, terminate/2, code_change/3]).

-define(SERVER, ?MODULE).

-record(state, {count = 0 :: integer()}).

%%%===================================================================
%%% API
%%%===================================================================

start_link() ->
    gen_server:start_link({local, ?SERVER}, ?MODULE, [], []).

get_count() ->
    gen_server:call(?SERVER, get_count).

increment() ->
    gen_server:cast(?SERVER, increment).

decrement() ->
    gen_server:cast(?SERVER, decrement).

set_count(Value) when is_integer(Value) ->
    gen_server:cast(?SERVER, {set_count, Value}).

%%%===================================================================
%%% gen_server callbacks
%%%===================================================================

init([]) ->
    {ok, #state{count = 0}}.

handle_call(get_count, _From, State = #state{count = Count}) ->
    {reply, Count, State};

handle_call(_Request, _From, State) ->
    {reply, ok, State}.

handle_cast(increment, State = #state{count = Count}) ->
    {noreply, State#state{count = Count + 1}};

handle_cast(decrement, State = #state{count = Count}) ->
    {noreply, State#state{count = Count - 1}};

handle_cast({set_count, Value}, State) ->
    {noreply, State#state{count = Value}};

handle_cast(_Request, State) ->
    {noreply, State}.

handle_info(_Info, State) ->
    {noreply, State}.

terminate(_Reason, _State) ->
    ok.

code_change(_OldVsn, State, _Extra) ->
    {ok, State}.

%%%===================================================================
%%% Internal functions
%%%===================================================================
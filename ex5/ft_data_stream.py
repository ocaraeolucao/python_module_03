import random
import typing


def gen_event() -> typing.Generator:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim",
               "release", "use"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(event_list: list) -> typing.Generator:
    while len(event_list) > 0:
        idx = random.randrange(len(event_list))
        event = event_list.pop(idx)
        yield event


def main():
    print("=== Game Data Stream Processor ===")
    event_stream = gen_event()
    for i in range(1000):
        event = next(event_stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    events_10 = []
    for _ in range(10):
        events_10.append(next(event_stream))
    print(f"Built list of 10 events: {events_10}")
    for event in consume_event(events_10):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_10}")


if __name__ == "__main__":
    main()

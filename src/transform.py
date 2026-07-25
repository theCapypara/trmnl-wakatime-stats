def run(input):
    # Make sure the Payload doesn't exceed the limit
    if "data" in input:
        for key in ("dependencies", "operating_systems", "projects", "machines"):
            if key in input["data"]:
                input["data"][key] = input["data"][key][:75]
        for key in ("languages",):
            if key in input["data"]:
                input["data"][key] = input["data"][key][:150]
    return input

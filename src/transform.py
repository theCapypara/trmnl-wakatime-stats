def run(input):
    if "data" not in input:
        return {"errors": [
            f"WakaTime did not return any data."
        ]}
    elif input["data"]["status"] != "ok":
        return {"errors": [
            f"WakaTime does not have the stats calculated yet. Current status: {input["data"]["status"]} "
            f"({input["data"]["percent_calculated"] if "percent_calculated" in input["data"] else 0}%)."
        ]}
    else:
        # Make sure the Payload doesn't exceed the limit
        for key in ("dependencies", "operating_systems", "projects", "machines"):
            if key in input["data"]:
                input["data"][key] = input["data"][key][:75]
        for key in ("languages",):
            if key in input["data"]:
                input["data"][key] = input["data"][key][:150]
    return input

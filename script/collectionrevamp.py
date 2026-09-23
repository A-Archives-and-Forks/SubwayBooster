import json

input_file_path = "temp/input/collectionsrevamp_data.json"
output_file_path = "src/profile/collectionsrevamp.json"


def process_collection(collections):
    state = {}
    for collection in collections:
        state[collection["id"]] = {
            "id": collection["id"],
            "items": {
                item["id"]: {
                    "id": item["id"],
                    "type": item["type"],
                    "unlockedAt": "1970-01-01T00:00:00Z",
                    "hasSeenUnlock": True,
                }
                for item in collection["items"]
            },
        }
    return state


if __name__ == "__main__":
    with open(input_file_path, "r", encoding="utf-8") as data_file:
        collections_data = json.load(data_file)

    collections_state = process_collection(collections_data.get("collections", []))

    reward_track_states = [{} for _ in range(collections_data.get("rewardTiers", 0))]

    crew_track_id = collections_data.get(
        "crewCapsuleRewardTrackId", "crew_capsule_reward_track"
    )

    data = {
        "lastSaved": "1970-01-01T00:00:00Z",
        "collectionsState": collections_state,
        "rewardTrackStates": reward_track_states,
        "managerExecutedForTheFirstTime": True,
        "isOnboardingFlowPlayed": True,
        "lastUpdate": "1970-01-01T00:00:00Z",
        "crewCapsRewardTrackStates": {crew_track_id: {}},
        "collectionRevampPreRolledRewardModel": {},
    }

    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump({"version": 1, "data": data}, f, indent=2)

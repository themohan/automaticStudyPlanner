schema = [
    {
        "noOfDays": "5",
        "noOfSubject": "4",
        "noOfHoursEachDay": "4",
        "chaptersInfo": [
            {
                "subject": "Maths",
                "difficulty": "Medium",
                "noOfChapters": "7",
            },
            {
                "subject": "English",
                "difficulty": "Easy",
                "noOfChapters": "8",
            },
            {
                "subject": "History",
                "difficulty": "Medium",
                "noOfChapters": "5",
            },
            {
                "subject": "Geography",
                "difficulty": "Hard",
                "noOfChapters": "3",
            },
        ],
    },
]

DIFFCULTY_HOURS_DISTRIBUTION = {
    "Easy": 1,
    "Medium": 2,
    "Hard": 3,
}
MAX_SUBJECT_DAY = 2

totalAvailableHours = int(schema[0]["noOfDays"]) * int(schema[0]["noOfHoursEachDay"])

requiredHours = 0
chapterInfoModified = []
for object in schema[0]["chaptersInfo"]:
    currentSubjectHours = DIFFCULTY_HOURS_DISTRIBUTION[object["difficulty"]] * int(object["noOfChapters"])
    requiredHours += currentSubjectHours

    modified_object = object.copy()
    modified_object["subjectHour"] = currentSubjectHours
    chapterInfoModified.append(modified_object)

weighted_factor = totalAvailableHours / requiredHours

chapterInfoModified = [
    {
        **object,
        "availableSubjectHours": round(weighted_factor * object["subjectHour"]),
        "perUnitTime": (weighted_factor * object["subjectHour"]) / int(object["noOfChapters"]),
    }
    for object in chapterInfoModified
]

# create subject chapter map
chapterObject = []

for chap in chapterInfoModified:
    for i in range(1, int(chap["noOfChapters"]) + 1):
        individualObject = {
            "subject": chap["subject"],
            "chapter": i,
            "status": False,
            "time": round(chap["perUnitTime"] * 2) / 2,  # rounding off to nearest 0.5
        }
        chapterObject.append(individualObject)

displayObject = []
cumm_index = 0
for i in range(int(schema[0]["noOfDays"])):
    cummulativeTime = 0
    dayObject = []
    while cummulativeTime < int(schema[0]["noOfHoursEachDay"]):
        cummulativeTime += chapterObject[cumm_index]["time"]

        dayObject.append({
            "subject": chapterObject[cumm_index]["subject"],
            "chapter": chapterObject[cumm_index]["chapter"],
        })
        cumm_index += 1

    displayObject.append(dayObject)

import json
print(json.dumps(displayObject, indent=2))


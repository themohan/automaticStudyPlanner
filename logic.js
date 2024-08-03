const schema = [
  {
    noOfDays: "5",
    noOfSubject: "4",
    noOfHoursEachDay: "4",
    chaptersInfo: [
      {
        subject: "Maths",
        difficulty: "Medium",
        noOfChapters: "7",
      },
      {
        subject: "English",
        difficulty: "Easy",
        noOfChapters: "8",
      },
      {
        subject: "History",
        difficulty: "Medium",
        noOfChapters: "5",
      },
      {
        subject: "Geography",
        difficulty: "Hard",
        noOfChapters: "3",
      },
    ],
  },
];
const DIFFCULTY_HOURS_DISTRIBUTION = {
  Easy: 1,
  Medium: 2,
  Hard: 3,
};
const MAX_SUBJECT_DAY = 2;

const totalAvailableHours =
  Number(schema[0].noOfDays) * Number(schema[0].noOfHoursEachDay);

let requiredHours = 0;
let chapterInfoModified = schema[0].chaptersInfo.map((object) => {
  let currentSubjectHours =
    DIFFCULTY_HOURS_DISTRIBUTION[object.difficulty] * object.noOfChapters;
  requiredHours = requiredHours + currentSubjectHours;

  return {
    ...object,
    subjectHour: currentSubjectHours,
  };
});

const weighted_factor = totalAvailableHours / requiredHours;
// const timeFactor =

chapterInfoModified = chapterInfoModified.map((object) => {
  return {
    ...object,
    availableSubjectHours: Math.round(
      Number(weighted_factor) * Number(object.subjectHour)
    ),
    perUnitTime:
      (Number(weighted_factor) * Number(object.subjectHour)) /
      object.noOfChapters,
  };
});

// create subject chapter map
let chapterObject = [];

const subjectChapterSchema = chapterInfoModified.map((chap) => {
  //   chapterObject.subject = chap.subject;
  //   chapterObject.chapterStatus = [];
  for (let i = 1; i <= chap.noOfChapters; i++) {
    let individualObject = {
      subject: chap.subject,
      chapter: i,
      status: false,
      time: Math.round(chap.perUnitTime * 2) / 2, //rounding off to nearest 0.5
    };
    chapterObject.push(individualObject);
  }
  return chapterObject;
});

// console.log(JSON.stringify(chapterObject, null, 2));

// console.log(JSON.stringify(chapterInfoModified, null, 2));

let displayObject = [];
let cumm_index = 0;
for (let i = 0; i < schema[0].noOfDays; i++) {
  let cummulativeTime = 0;

  console.log("i", i);
  let dayObject = [];
  while (cummulativeTime < schema[0].noOfHoursEachDay) {
    // console.log(chapterObject[cumm_index]);
    cummulativeTime += chapterObject[cumm_index]?.time;

    dayObject.push({
      subject: chapterObject[cumm_index]?.subject,
      chapter: chapterObject[cumm_index]?.chapter,
    });
    cumm_index = cumm_index + 1;
  }

  displayObject.push(dayObject);
}

console.log(JSON.stringify(displayObject, null, 2));

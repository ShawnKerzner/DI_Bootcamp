const gameInfo = [
 {
   username: "john",
   team: "red",
   score: 5,
   items: ["ball", "book", "pen"]
 },
 {
   username: "becky",
   team: "blue",
   score: 10,
   items: ["tape", "backpack", "pen"]
 },
 {
   username: "susy",
   team: "red",
   score: 55,
   items: ["ball", "eraser", "pen"]
 },
 {
   username: "tyson",
   team: "green",
   score: 1,
   items: ["book", "pen"]
 },
];

const usernames = gameInfo.forEach((user) => console.log(`${user.username}!`))

const winners = gameInfo.forEach((user) => (user.score > 5 ? console.log(user.username) : false));

const totalScore = gameInfo.reduce((sum, user) => sum + user.score, 0);
console.log(totalScore);
    
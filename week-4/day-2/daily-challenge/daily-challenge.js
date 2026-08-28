class Video {
    constructor(title, uploader, time) {
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }
    watch() {
        console.log(`${this.uploader} watched all ${this.time} of ${this.title}`);
    }
}

let lotr = new Video("Lord of The Rings", "Shawn", "2000000 seconds");
let starWars = new Video("Starwars", "Daniel", "4567893426 seconds");
lotr.watch();
starWars.watch();

videoArray = [{ title: "movie1", uploader: "user1", time: "100 seconds" },
{ title: "movie2", uploader: "user2", time: "206 seconds" },
{ title: "movie3", uploader: "user3", time: "190 seconds" },
{ title: "movie4", uploader: "user4", time: "10 seconds" },
{ title: "movie5", uploader: "user5", time: "789 seconds" }];

for (let video of videoArray) {
    let videoInstance = new Video(video["title"], video["uploader"], video["time"])
}
let track_index = 0;

let audio = [
    {
        file: new Audio('./assets/songs/track2.mp3'),
        cover: "./assets/songs/cover2.jpg",
        name: "Answer: Love Myself",
        artist: "BTS"
    },
    {
        file: new Audio('./assets/songs/track1.mp3'),
        cover: "./assets/songs/cover1.jpeg",
        name: "Make me feel",
        artist: "Janelle Monae"
    },
    {
        file: new Audio('./assets/songs/track3.mp3'),
        cover: "./assets/songs/cover3.jpg",
        name: "Volcanic Love",
        artist: "The Aces"
    },
    {
        file: new Audio('./assets/songs/track4.mp3'),
        cover: "./assets/songs/cover4.jpeg",
        name: "Little Things",
        artist: "One Direction"
    },
    {
        file: new Audio('./assets/songs/track5.mp3'),
        cover: "./assets/songs/cover5.jpg",
        name: "Favourite Crime",
        artist: "Olivia Rodrigo"
    },
    {
        file: new Audio('./assets/songs/track6.mp3'),
        cover: "./assets/songs/cover6.jpeg",
        name: "Friday I'm in Love",
        artist: "The Cure"
    },
    {
        file: new Audio('./assets/songs/track7.mp3'),
        cover: "./assets/songs/cover7.jpg",
        name: "Arabella",
        artist: "Arctic Monkeys"
    },
    {
        file: new Audio('./assets/songs/Track8.mp3'),
        cover: "./assets/songs/Cover8.jpeg",
        name: "Eventually",
        artist: "Tame Impala"
    },
    {
        file: new Audio('./assets/songs/Track9.mp3'),
        cover: "./assets/songs/Cover9.jpeg",
        name: "18",
        artist: "One Direction"
    },
    {
        file: new Audio('./assets/songs/Track10.mp3'),
        cover: "./assets/songs/Cover10.jpg",
        name: "I heard you're married",
        artist: "The Weeknd (ft. Lil Wayne)"
    },
    {
        file: new Audio('./assets/songs/Track11.mp3'),
        cover: "./assets/songs/Cover11.jpeg",
        name: "hornyloveskickmess",
        artist: "Girl in Red"
    },
    {
        file: new Audio('./assets/songs/Track12.mp3'),
        cover: "./assets/songs/Cover12.jpeg",
        name: "Christmas Tree",
        artist: "V"
    },
    {
        file: new Audio('./assets/songs/Track13.mp3'),
        cover: "./assets/songs/Cover13.jpeg",
        name: "Story of my life",
        artist: "One Direction"
    },
    {
        file: new Audio('./assets/songs/Track14.mp3'),
        cover: "./assets/songs/Cover14.jpeg",
        name: "Always a dream",
        artist: "Dafna"
    },
    {
        file: new Audio('./assets/songs/Track15.mp3'),
        cover: "./assets/songs/Cover15.jpeg",
        name: "Avoid Things",
        artist: "Tems"
    },
    {
        file: new Audio('./assets/songs/Track16.mp3'),
        cover: "./assets/songs/Cover16.jpeg",
        name: "Human",
        artist: "Dodie and Tom Walker"
    },
    {
        file: new Audio('./assets/songs/Track17.mp3'),
        cover: "./assets/songs/Cover17.png",
        name: "Polaroid Love",
        artist: "ENHYPEN"
    },
    {
        file: new Audio('./assets/songs/Track18.mp3'),
        cover: "./assets/songs/Cover18.jpeg",
        name: "Sex money feelings die",
        artist: "Lykke Li"
    }

]

let isPlaying = false;
let playButton = document.getElementById("button__play");
let pauseButton = document.getElementById("button__pause");

let songName = document.querySelector(".song__name");
let artistName = document.querySelector(".artist__name");
let coverImage = document.querySelector("img.cover__image");

const audio_toggle = () => {
    if (isPlaying) {
        playButton.style.display = "inline-block"
        pauseButton.style.display = "none"
    } else {
        playButton.style.display = "none"
        pauseButton.style.display = "inline-block"
    }
    isPlaying = !isPlaying
}

const updateSongInfo = (track_i) => {
    let curr_track = audio[track_i];
    songName.innerHTML = curr_track.name;
    artistName.innerHTML = curr_track.artist;
    coverImage.setAttribute("src", curr_track.cover);
}

const play = () => {
    audio_toggle();
    audio[track_index].file.volume = 0.1
    audio[track_index].file.play();
    updateSongInfo(track_index);
    playButton.style.display = "none"
    pauseButton.style.display = "inline-block"
    audio[track_index].file.onended = function () {
        track_index += 1
        if (track_index >= audio.length) track_index = 0
        audio[track_index].file.volume = 0.1
        audio[track_index].file.play()
    }
}

const pause = () => {
    audio_toggle();
    audio[track_index].file.pause();
    playButton.style.display = "inline-block"
    pauseButton.style.display = "none"
}

const next_song = () => {
    audio[track_index].file.pause();
    audio[track_index].file.currentTime = 0;
    track_index = track_index === audio.length - 1 ? 0 : track_index + 1;
    audio[track_index].file.volume = 0.1
    audio[track_index].file.play();
    playButton.style.display = "none"
    pauseButton.style.display = "inline-block"
    updateSongInfo(track_index);
}

const previous_song = () => {
    audio[track_index].file.pause();
    audio[track_index].file.currentTime = 0;
    track_index = track_index === 0 ? audio.length - 1 : track_index - 1;
    audio[track_index].file.volume = 0.1
    audio[track_index].file.play();
    playButton.style.display = "none"
    pauseButton.style.display = "inline-block"
    updateSongInfo(track_index);
}

updateSongInfo(0);
//play();
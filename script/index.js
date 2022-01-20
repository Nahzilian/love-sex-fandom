let track_index = 0;

let audio = [
    {
        file: new Audio('./assets/songs/track1.mp3'),
        cover: "./assets/songs/blue.jpg",
        name: "Entertain me",
        artist: "Ylona Garcia"
    },
    {
        file: new Audio('./assets/songs/track2.mp3'),
        cover: "./assets/songs/blue.jpg",
        name: "Put Your Records On",
        artist: "Ritt Momney",
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
    coverImage.setAttribute("src",curr_track.cover);
}

const play = () => {
    audio_toggle();
    audio[track_index].file.play();
    updateSongInfo(track_index);
    audio[track_index].file.onended = function () {
        track_index += 1
        if (track_index >= audio.length) track_index = 0
        audio[track_index].file.play()
    }
}

const pause = () => {
    audio_toggle();
    audio[track_index].file.pause();
}

const next_song = () => {
    audio[track_index].file.pause();
    audio[track_index].file.currentTime = 0;
    track_index = track_index === audio.length - 1 ? 0 : track_index + 1;
    audio[track_index].file.play();
    updateSongInfo(track_index);
}

const previous_song = () => {
    audio[track_index].file.pause();
    audio[track_index].file.currentTime = 0;
    track_index = track_index === 0 ? audio.length - 1 : track_index - 1;
    audio[track_index].file.play();
    updateSongInfo(track_index);
}

updateSongInfo(0);
//play();
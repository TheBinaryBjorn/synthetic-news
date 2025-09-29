"use client";
import Image from "next/image";
import { useState } from "react";
export default function NowPlaying() {
  const podcasts = [
    {
      title: "The future of AI",
      thumbnail: "/TheFutureOfAI.png",
      topic: "Artificial Intelligence",
    },
  ];
  const [mediaNowPlaying, setMediaNowPlaying] = useState(podcasts[0]);
  return (
    <div className="shadow-md bg-white/1 border-white/10 border-1 backdrop-blur-2xl py-1 rounded-full flex flex-row items-center justify-center gap-4 px-1">
      {/*Image*/}
      <Image
        src={mediaNowPlaying.thumbnail}
        alt={mediaNowPlaying.title}
        width="64"
        height="64"
        className="rounded-full"
      />
      {/*Data*/}
      <div className="text-white flex flex-col gap-1 mr-4">
        <h1 className="text-sm font-semibold">{mediaNowPlaying.title}</h1>
        <h2 className="text-white/70 text-xs">{mediaNowPlaying.topic}</h2>
      </div>
    </div>
  );
}

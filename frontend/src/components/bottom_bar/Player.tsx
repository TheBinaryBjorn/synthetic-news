"use client";
import { Play, Pause, SkipBack, SkipForward } from "lucide-react";
import { useState } from "react";

export default function Player() {
  const [isPlaying, setIsPlaying] = useState(false);
  return (
    <div className="flex flex-row gap-6 bg-gray-400">
      <SkipBack/>
      <button
        onClick={() => setIsPlaying(!isPlaying)}
        className="p-2 bg-white/20 backdrop-blur-xl rounded-full text-white hover:bg-white/30 hover:cursor-pointer"
      >
        {isPlaying ? <Play /> : <Pause />}
      </button>
      <SkipForward/>
    </div>
  );
}

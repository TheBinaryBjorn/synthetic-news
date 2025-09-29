"use client";
import { Play, Pause, SkipBack, SkipForward } from "lucide-react";
import { useState } from "react";
import { RoundedButton } from "../ui/Buttons";

export default function Player() {
  const [isPlaying, setIsPlaying] = useState(false);
  return (
    <div className="shadow-md flex flex-row rounded-full p-4 bg-white/20 border-white/20 border-1 items-center justify-between gap-4 text-white">
      <RoundedButton onClick={() => setIsPlaying(!isPlaying)}>
        <SkipBack />
      </RoundedButton>
      <RoundedButton onClick={() => setIsPlaying(!isPlaying)}>
        {isPlaying ? <Play /> : <Pause />}
      </RoundedButton>
      <RoundedButton onClick={() => setIsPlaying(!isPlaying)}>
        <SkipForward />
      </RoundedButton>
    </div>
  );
}


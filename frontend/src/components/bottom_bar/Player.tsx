"use client";
import { Play, Pause, SkipBack, SkipForward } from "lucide-react";
import { useState, ReactNode } from "react";

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

interface RoundedButtonProps {
  children: ReactNode;
  onClick?: () => void;
}

export function RoundedButton({ children, onClick }: RoundedButtonProps) {
  return (
    <button
      className="p-2 bg-white/1 backdrop-blur-xl rounded-full text-white hover:bg-white/30 hover:cursor-pointer duration-300 transition-all"
      onClick={onClick}
    >
      {children}
    </button>
  );
}

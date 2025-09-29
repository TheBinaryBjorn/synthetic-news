import { Volume2 } from "lucide-react";
export default function VolumeControl() {
  return (
    <div className="bg-white/20 p-4 text-white rounded-full shadow-md border-white/30 border-1 flex flex-col gap-3 items-center">
      <Volume2 />
      {/* Needs to be replaced with actual volume control */}
      <div className="w-16 h-1 bg-white/20 rounded-full overflow-hidden">
        <div className="h-full bg-white/60 w-3/4"></div>
      </div>
    </div>
  );
}

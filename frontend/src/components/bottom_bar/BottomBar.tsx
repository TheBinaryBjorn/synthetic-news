import NowPlaying from "./NowPlaying";
import Player from "./Player";
import VolumeControl from "./VolumeControl";

export default function BottomBar() {
  return (
    <div className="fixed bottom-0 w-screen h-20 border-t-1 bg-white border-gray-200 flex flex-row items-center justify-between px-8">
      <NowPlaying />
      <Player />
      <VolumeControl />
    </div>
  );
}

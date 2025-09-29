import NowPlaying from "./NowPlaying";
import Player from "./Player";
import VolumeControl from "./VolumeControl";

export default function BottomBar() {
  return (
    <div className="shadow-md rounded-full m-2 mx-auto bg-white/20 backdrop-blur-2xl fixed bottom-0 right-0 left-0 w-99/100 border-t-1 border-white/20 flex flex-row items-center justify-between p-1">
      <div className="flex-1 flex justify-start">
        <NowPlaying />
      </div>
      <div className="flex-shrink-0">
        <Player />
      </div>
      <div className="flex-1 flex justify-end">
        <VolumeControl />
      </div>
    </div>
  );
}

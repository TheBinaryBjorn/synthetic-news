import DarkLightSwitch from "./DarkLightSwitch";
import HomeButton from "./HomeButton";
import ProfileButton from "./ProfileButton";
import SearchBar from "./SearchBar";
import { RoundedButton } from "../ui/Buttons";

export default function Navbar() {
  return (
    <div className="fixed top-0 w-screen px-2">
      <nav className="backdrop-blur-sm mx-auto z-50 bg-white/20 border-white/30 border-1 shadow-md flex flex-row justify-between items-center rounded-full mt-2 p-2 px-4">
        <div className="flex-1 flex justify-start">
          <RoundedButton>
            <HomeButton />
          </RoundedButton>
        </div>
        <div className="flex-1 flex shrink-0">
          <SearchBar />
        </div>
        <div className="flex-1 justify-end flex flex-row items-center gap-4">
          <DarkLightSwitch />
          <ProfileButton />
        </div>
      </nav>
    </div>
  );
}

import DarkLightSwitch from "./DarkLightSwitch";
import HomeButton from "./HomeButton";
import ProfileButton from "./ProfileButton";
import SearchBar from "./SearchBar";

export default function Navbar() {
  return (
    <nav className="fixed dark:bg-black dark:text-white px-8 top-0 w-screen z-50 bg-white h-15 shadow-md flex flex-row justify-between items-center">
      <div className="flex-1 flex justify-start">
        <HomeButton />
      </div>
      <div className="flex-1 flex shrink-0">
      <SearchBar />
      </div>
      <div className="flex-1 justify-end flex flex-row items-center gap-4">
        <DarkLightSwitch />
        <ProfileButton />
      </div>
    </nav>
  );
}

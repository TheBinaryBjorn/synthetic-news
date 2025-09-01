import DarkLightSwitch from "./DarkLightSwitch";
import HomeButton from "./HomeButton";
import ProfileButton from "./ProfileButton";
import SearchBar from "./SearchBar";

export default function Navbar() {
  return (
    <nav className="fixed dark:bg-black dark:text-white px-8 top-0 w-screen z-50 bg-white h-15 shadow-md flex flex-row justify-between items-center">
      <HomeButton />
      <SearchBar />
      <div className="flex flex-row items-center gap-4">
        <DarkLightSwitch />
        <ProfileButton />
      </div>
    </nav>
  );
}

import DarkLightSwitch from "./DarkLightSwitch";
import HomeButton from "./HomeButton";
import ProfileButton from "./ProfileButton";
import SearchBar from "./SearchBar";

export default function Navbar() {
  return (
    <nav className="fixed px-8 top-0 w-screen z-50 bg-white h-20 shadow-md border-b-1 border-gray-200 flex flex-row justify-between items-center">
      <HomeButton />
      <SearchBar />
      <div className="flex flex-row items-center gap-4">
        <DarkLightSwitch />
        <ProfileButton />
      </div>
    </nav>
  );
}

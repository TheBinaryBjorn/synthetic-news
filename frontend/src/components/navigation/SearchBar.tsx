import Image from "next/image";
import { Search } from "lucide-react";
export default function SearchBar() {
  return (
    <div className="text-white border-1 border-white/30 bg-white/10 shadow-md w-md flex flex-row items-center rounded-full px-4 py-2 hover:brightness-150 duration-300">
      <Search/>
      <input
        className="ml-3 duration-300 w-full"
        placeholder="What topic interests you today?"
      ></input>
    </div>
  );
}

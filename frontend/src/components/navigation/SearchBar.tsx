import Image from "next/image";
export default function SearchBar() {
  return (
    <div className="w-md flex flex-row items-center rounded-full bg-stone-800 px-4 py-2 hover:brightness-150 duration-300">
      <Image src="/icons/search-7525.svg" width="24" height="24" alt="Search" />
      <input
        className="ml-3 duration-300 w-full"
        placeholder="What topic interests you today?"
      ></input>

    </div>
  );
}

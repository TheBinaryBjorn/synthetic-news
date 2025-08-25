import Link from "next/link";
import Image from "next/image";

export default function HomeButton() {
  return (
    <Link href="/" className="rounded-full p-3 dark:bg-stone-800 hover:brightness-150 bg-gray-200 duration-300 hover:scale-105">
      <Image src="/icons/home-175.svg" width="22" height="22" alt="Home" aria-label="Home" />
    </Link>
  );
}

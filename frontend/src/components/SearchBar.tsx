import { useEffect } from "react";
import styles from "../styles/SearchBar.module.css";

interface SearchBarProps {
    query: string;
    setQuery: React.Dispatch<React.SetStateAction<string>>;
    inputProps?: React.InputHTMLAttributes<HTMLInputElement>;
    pasteIconProps?: React.ImgHTMLAttributes<HTMLImageElement>;
    searchIconProps: React.ImgHTMLAttributes<HTMLImageElement>;
}

export const SearchBar = (props: SearchBarProps) => {
    return (
        <div className={styles.inputContainer}>
            <input className={styles.searchBar} {...props.inputProps} />
            <img
                src={require("../assets/paste.png")}
                alt="paste"
                height={20}
                width={20}
                className={[styles.searchBarIcon, styles.pasteIcon].join(" ")}
                {...props.pasteIconProps}
            />
            <img
                src={require("../assets/search.png")}
                alt="search"
                height={20}
                width={20}
                className={[styles.searchBarIcon, styles.searchIcon].join(" ")}
                {...props.searchIconProps}
            />
        </div>
    );
};

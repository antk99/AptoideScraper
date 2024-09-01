import { useState } from "react";
import { AppInfo } from "./components/AppInfo";
import useFetch from "./hooks/useFetch";
import styles from "./styles/App.module.css";
import { LoadingSpinner } from "./components/LoadingSpinner";
import { SearchBar } from "./components/SearchBar";

interface APIResponse {
    name: string;
    icon_url: string;
    version: string;
    num_downloads: string;
    release_date: string;
    description: string;
}

export const App = () => {
    const [url, setUrl] = useState<string>("");
    const { data, error, isLoading, fetchData } = useFetch<APIResponse>();

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => setUrl(e.target.value);

    const handlePaste = async () => {
        const text = await navigator.clipboard.readText();
        handleInputChange({ target: { value: text } } as React.ChangeEvent<HTMLInputElement>);
    };

    const handleSubmit = () => {
        fetchData(`aptoide?url=${url}`);
    };

    return (
        <div className={styles.container}>
            <div className={styles.hero}>
                <h1>Aptoide Webscraper</h1>
                <p>Search for an app on Aptoide and get its details.</p>
            </div>

            <SearchBar
                query={url}
                setQuery={setUrl}
                inputProps={{
                    type: "text",
                    placeholder: "https://app.en.aptoide.com/app",
                    onChange: handleInputChange,
                    value: url,
                    maxLength: 100,
                }}
                pasteIconProps={{ onClick: handlePaste }}
                searchIconProps={{ onClick: handleSubmit }}
            />

            {isLoading && <LoadingSpinner />}
            {!isLoading && error && <p className={styles.error}>{error}</p>}
            {!isLoading && !error && data && <AppInfo {...data} />}
        </div>
    );
};

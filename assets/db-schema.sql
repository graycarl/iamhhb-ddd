BEGIN;
-- Blog Table
CREATE TABLE blog (
    id CHAR(64) PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    sub_title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    content_type VARCHAR(20) NOT NULL,
    created_at DATETIME,
    updated_at DATETIME
);
-- Reading Table
CREATE TABLE reading_note (
    id INTEGER PRIMARY KEY,
    book_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    content_type VARCHAR(20) NOT NULL,
    created_at DATETIME,
    updated_at DATETIME
);
CREATE TABLE book (
    id INTEGER PRIMARY KEY,
    isbn CHAR(32) NULL,
    title VARCHAR(80) NOT NULL,
    sub_title VARCHAR(200) NULL,
    cover VARCHAR(200) NULL,
    created_at DATETIME
);
-- Wiki Page
CREATE TABLE wiki_page (
    id CHAR(64) PRIMARY KEY,
    title VARCHAR(80) NOT NULL,
    content TEXT NOT NULL,
    content_type VARCHAR(20) NOT NULL,
    created_at DATETIME,
    updated_at DATETIME
);
COMMIT;
